from aws_cdk import (
    aws_iam as iam,
    core,
)


class IAMRole(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        with open("iam-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        LambdaServiceRole = iam.Role(
            self,
            "Lambda_Service_Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSXrayFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchLogsFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSNSFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSBatchFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonEC2FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSStepFunctionsFullAccess")
            ],
            role_name="Lambda_Service_Role"
        )

        BatchJobsServiceRole = iam.Role(
            self,
            "BatchJobsServiceRole",
            assumed_by=iam.ServicePrincipal("batch.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSNSFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSBatchFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonECS_FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "IAMFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonEC2FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSQSFullAccess")
            ],
            role_name="Batchjob_Service_Role"
        )
        BatchComputeEnvServiceRole = iam.Role(
            self,
            "BatchComputeEnvServiceRole",
            assumed_by=iam.ServicePrincipal("batch.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchLogsFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSNSFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonECS_FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AutoScalingFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSBatchFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonEC2FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSQSFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSBatchServiceRole")
            ],
            role_name="Batch_Compute_Env_Service_Role"
        )
        StepFunctionsServiceRole = iam.Role(
            self,
            "StepFunctionsServiceRole",
            assumed_by=iam.ServicePrincipal("states.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSNSFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSBatchFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchEventsFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSLambdaExecute"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSLambdaFullAccess")
            ],
            role_name="Step_Functions_Service_Role"
        )
        CDKCodeBuildServiceRole = iam.Role(
            self,
            "CDKCodeBuildServiceRole",
            assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSCodeBuildAdminAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSLambda_FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSCloudFormationFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchLogsFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonVPCFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSBatchFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "IAMFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSStepFunctionsFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonEC2ContainerRegistryFullAccess")
            ],
            role_name="CDK_Code_Build_Service_Role"
        )


app = core.App()
IAMRole(app, "IAMRoles")
app.synth()
