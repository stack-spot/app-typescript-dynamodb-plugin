from pathlib import Path
from typing import List
from templateframework.metadata import Metadata
from templateframework.runner import run
from templateframework.template import Template
import subprocess

def read_file(file_path: Path):
    with file_path.open() as file:
        return file.readlines()

def write_in_stackfile(
        stackfile_path: Path,
        final_stackfile_lines: List[str],
        metadata: Metadata,
        source_dir_path: str
):
    with stackfile_path.open('w') as file_to_write:
        for line in final_stackfile_lines:
            file_to_write.write(line)
            if line.startswith('import * as cdk'):
                file_to_write.write(
                    'import { StackSpotDynamoDBTable } from \'@stackspot/cdk-component-dynamodb-typescript\';\n'
                )
            elif line.endswith('super(scope, id, props);\n'):
                file_to_write.write(
                    '\t\tnew StackSpotDynamoDBTable(this, \'' + metadata.inputs['table_name']+ '\', {\n' +
                    '\t\t\tgenerateRepository: true,\n' +
                    '\t\t\trepositoryGenerationConfiguration: {\n' +
                        '\t\t\t\ttracing: false\n' +
                        '\t\t\t\tsourceDir: \'src\'\n' +
                    '\t\t\t}\n' +
                    '\t\t});\n'
                )

def execute_npm_install(infra_resource_path: str, source_dir_path: str):
    subprocess.run(['npm', 'install'], cwd=infra_resource_path)
    subprocess.run(
        ['npm', 'install', '-S', '@aws-cdk/aws-dynamodb @stackspot/cdk-component-dynamodb-typescript@^0.2.1'],
        cwd=infra_resource_path
    )
    subprocess.run(['npm', 'run', 'build'], cwd=infra_resource_path)
    subprocess.run(['npm', 'run', 'local', 'synth'], cwd=infra_resource_path)
    subprocess.run(['npm', 'install', '-S'], cwd=source_dir_path)
    subprocess.run(['npm', 'run', 'build'], cwd=source_dir_path)

class InitDynamoDBPlugin(Template):
    def post_hook(self, metadata: Metadata):
        resource_path = metadata.target_path.joinpath('infra/lib')
        main_stack_code_file = resource_path.joinpath('service-name-service-stack.ts')
        stackfile_lines = read_file(main_stack_code_file)

        source_dir_path_str = metadata.inputs['source_dir']
        infra_resource_path = metadata.target_path.joinpath('infra')
        source_dir_path = infra_resource_path.joinpath(source_dir_path_str)

        
        write_in_stackfile(main_stack_code_file, stackfile_lines, metadata, source_dir_path_str)

        execute_npm_install(infra_resource_path, source_dir_path)


if __name__ == '__main__':
    run(InitDynamoDBPlugin())