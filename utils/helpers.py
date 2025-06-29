import importlib

def load_formulas(class_level, subject):
    try:
        mod_path = f"formulas.class{class_level}.{subject.lower()}"
        module = importlib.import_module(mod_path)
        return module.formulas
    except Exception as e:
        return {"Error": f"Formulas not available for this combination: {e}"}
