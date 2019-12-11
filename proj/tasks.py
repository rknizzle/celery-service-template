"""
Celery Async tasks definitions

"""
# ============================================================================
# necessary imports
# ============================================================================
import random
import time

import celery

from proj import app


# ============================================================================
# tasks defintions
# ============================================================================
@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    total = random.randint(5, 40)
    for i in range(total):
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': 'processing...'})

        time.sleep(1)

    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}
# ============================================================================
# EOF
# ============================================================================
