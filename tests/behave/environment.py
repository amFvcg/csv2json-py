import tempfile
import os


def before_scenario(context, scenario):
    context.original_wd = os.getcwd()
    context.temp_dir = tempfile.mkdtemp()
    os.chdir(context.temp_dir)

def after_scenario(context, scenario):
    from shutil import rmtree
    os.chdir(context.original_wd)
    rmtree(context.temp_dir)
