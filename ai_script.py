from pyke import knowledge_engine
import os
print(os.__file__)
engine = knowledge_engine.engine("es/")
print(engine)
engine.activate('rules')
engine.get_kb('facts').dump_specific_facts()
