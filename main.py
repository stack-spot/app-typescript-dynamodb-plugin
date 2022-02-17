from templateframework.metadata import Metadata
from templateframework.runner import run
from templateframework.template import Template
import subprocess


def execute_npm_install(infra_resource_path: str, source_dir_path: str):
    subprocess.run(['npm', 'install'], cwd=infra_resource_path)
    subprocess.run(
        ['npm', 'install', '@aws-cdk/aws-dynamodb', '@stackspot/cdk-component-dynamodb-typescript@^0.2.1'],
        cwd=infra_resource_path
    )
    subprocess.run(['npm', 'run', 'build'], cwd=infra_resource_path)
    subprocess.run(['npm', 'run', 'local', 'synth'], cwd=infra_resource_path)
    subprocess.run(['npm', 'install'], cwd=source_dir_path)
    subprocess.run(['npm', 'run', 'build'], cwd=source_dir_path)


class InitDynamoDBPlugin(Template):
    def post_hook(self, metadata: Metadata):
        # source_dir_path_str = metadata.inputs['source_dir']
        infra_resource_path = metadata.target_path.joinpath('infra')
        source_dir_path = infra_resource_path.joinpath('src')
        execute_npm_install(infra_resource_path, source_dir_path)


if __name__ == '__main__':
    run(InitDynamoDBPlugin())
