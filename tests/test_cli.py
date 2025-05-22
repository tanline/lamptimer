from lamptimer.cli import cli

def test_cli_prints_hello(capsys):
    cli()
    captured = capsys.readouterr()
    assert "Hello from lamptimer!" in captured.out
