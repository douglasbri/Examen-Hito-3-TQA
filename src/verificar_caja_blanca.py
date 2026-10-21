"""Ejecuta los 3 casos solicitados y 2 ampliaciones; usa la función original."""
import ast
import json
from pathlib import Path
import sys
from validar_compra import validar_compra

root = Path(__file__).resolve().parents[1]
source = Path(__file__).with_name('validar_compra.py')
tree = ast.parse(source.read_text(encoding='utf-8'))
decisions = {node.lineno:(f'D{i}',node.body[0].lineno) for i,node in enumerate([n for n in tree.body[0].body if isinstance(n,ast.If)],1)}
cases = [
 ('CB-001',(17,True,100,50),'Compra no permitida: edad'),
 ('CB-002',(18,False,100,50),'Compra no permitida: cuenta'),
 ('CB-003',(18,True,100,100),'Compra aprobada'),
 ('CB-004',(18,True,50,100),'Compra rechazada'),
 ('CB-005',(18,True,0,0),'Compra rechazada'),
]
results=[]
for id,args,expected in cases:
 lines=[]
 def trace(frame,event,arg):
  if frame.f_code is validar_compra.__code__ and event=='line': lines.append(frame.f_lineno)
  return trace
 sys.settrace(trace)
 try: actual=validar_compra(*args)
 finally: sys.settrace(None)
 assert actual==expected,(id,actual,expected)
 observed={}
 for a,b in zip(lines,lines[1:]):
  if a in decisions:
   name,true_line=decisions[a]; observed[name]=(b==true_line)
 results.append(dict(id=id,entradas=list(args),esperado=expected,obtenido=actual,estado='PASS',lineas_ejecutadas=lines,decisiones=observed))
def coverage(rows):
 outcomes={(k,v) for row in rows for k,v in row['decisiones'].items()}
 return {'resultados_cubiertos':len(outcomes),'resultados_totales':6,'porcentaje':round(len(outcomes)/6*100,2)}
report={'criterio':'decisiones','casos':results,'tres_solicitados':coverage(results[:3]),'con_ajuste_CB004':coverage(results[:4]),'nota':'CB-005 es una ampliación para condiciones simples; no es necesaria para 100% de decisiones.'}
(root/'evidencias/caja_blanca_ejecucion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
