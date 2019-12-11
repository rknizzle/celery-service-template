"""
Flask views

"""
# ============================================================================
# necessary imports
# ============================================================================
from flask import session, request, render_template, flash, jsonify, url_for
from flask import redirect

from proj import app
from proj.tasks import long_task


# ============================================================================
# views
# ============================================================================



@app.route('/longtask', methods=['POST'])
def longtask():
    """
    Route for starting long background task.

    """
    task = long_task.apply_async()

    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    """Celery task status notifier."""
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job has not started yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending..'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this's the exception raised
        }

    return jsonify(response)
# ============================================================================
# EOF
# ============================================================================
