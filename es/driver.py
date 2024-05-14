import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def test():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('rules') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        engine.get_kb('facts').dump_specific_facts()

        with engine.prove_goal('rules.direct_batch_supplier($supplier,$units)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should bring: %s" % (vars['suppliers'],vars['units'])) #STUDENTS: you will need to edit this line
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print("done")
    #engine.print_stats()


def bc_test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('questions_rules') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with engine.prove_goal('question_rules.what_to_bring($bring)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should bring: %s" % (vars['bring'])) #STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print("done")