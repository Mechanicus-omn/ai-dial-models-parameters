from task.app.main import run

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    stop=["\n\n"]
)
