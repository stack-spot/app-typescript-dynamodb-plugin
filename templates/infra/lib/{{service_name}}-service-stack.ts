import * as cdk from '@aws-cdk/core';
import { StackSpotTypescriptDynamoDBPlugin } from "./stack-spot-typescript-dynamodb-plugin";

export class {{service_name|title|replace("-", "")}}ServiceStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new StackSpotTypescriptDynamoDBPlugin(this);
  }
}
