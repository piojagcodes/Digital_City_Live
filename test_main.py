from typer.testing import CliRunner
from main import app


runner = CliRunner()

def test_greet_command():
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice\n" in result.output
    
def test_goodbye_command():
    result = runner.invoke(app, ["goodbye","Alice"])
    assert result.exit_code == 0
    assert "Bye Alice\n" in result.output
    
def test_goodbye_command_formal():
    result = runner.invoke(app, ["goodbye","Alice","--formal"])
    assert result.exit_code == 0
    assert "Goodbye Ms. Alice. Have a good day\n" in result.output