from celery import shared_task
from .models import PipelineExecution
import time

@shared_task
def execute_pipeline_stage(execution_id, stage_config):
    try:
        execution = PipelineExecution.objects.get(id=execution_id)
        execution.status = 'RUNNING'
        execution.save()
        
        # Simulate stage execution (Checkout, Install, Test, Build, Deploy)
        time.sleep(2)
        
        execution.logs += f"\\nExecuted stage: {stage_config.get('name', 'Unknown')}"
        execution.save()
        return True
    except PipelineExecution.DoesNotExist:
        return False

@shared_task
def run_full_pipeline(execution_id):
    try:
        execution = PipelineExecution.objects.get(id=execution_id)
        config = execution.pipeline.configuration
        
        stages = config.get('stages', [])
        for stage in stages:
            success = execute_pipeline_stage(execution_id, stage)
            if not success:
                execution.status = 'FAILED'
                execution.save()
                return False
                
        execution.status = 'SUCCESS'
        execution.save()
        return True
    except Exception as e:
        return False
