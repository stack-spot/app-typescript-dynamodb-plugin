import * as cdk from '@aws-cdk/core';
import { StackSpotDynamoDBTable } from "@stackspot/cdk-component-dynamodb-typescript";
import { AttributeType } from "@aws-cdk/aws-dynamodb/lib/table";

export class StackSpotTypescriptDynamoDBPlugin {
    constructor(scope: cdk.Construct) {
        new StackSpotDynamoDBTable(scope, 'StackSpotDynamoDBTable', {
            generateRepository: true,
            repositoryGenerationConfiguration: {
                tracing: false,
                sourceDir: 'src',
            },
            tableConfiguration: {
                tableName: '{{table_name}}',
                partitionKey: {
                    name: 'id',
                    type: AttributeType.NUMBER
                }
            }
        });
    }
}
