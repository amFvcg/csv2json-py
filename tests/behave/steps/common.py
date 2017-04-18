from behave import given, when, then


@given('csv file {filename} with input')
def step_impl(context, filename):
    with open(filename, 'w') as f:
        f.write(context.text)


@when('we run {command}')
def step_impl(context, command):
    import subprocess
    s = subprocess.Popen(command.split())
    retcode = s.wait()
    stdout, stderr = s.communicate()


@then('we expect to have file {filename} with content')
def step_impl(context, filename):
    import json
    expected = json.loads(context.text)
    with open(filename) as f:
        result = json.load(f)
        assert expected == result,\
            '\n\tExpected : {},\n\tgot      : {}'.format(expected, result)
