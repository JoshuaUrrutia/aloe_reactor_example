from reactors.utils import Reactor, agaveutils
from agavepy.agave import Agave
import json
import pprint
import copy


# def parseCallback(r):
#     ag = r.client
#     assert ag is not None, "parseCallback: Agave client is not present"
#     context = r.context
#     lastAction = urllib.unquote_plus(context.lastAction)
#     queues = urllib.unquote_plus(context.queues)
#     dataset = urllib.unquote_plus(context.dataset)
#     archivePath = urllib.unquote_plus(context.archivePath)
#     archiveSystem = urllib.unquote_plus(context.archiveSystem)
#     manifestURL = urllib.unquote_plus(context.manifestURL)
#     pipeline_uuid = urllib.unquote_plus(context.pipeline_uuid)
#     assert lastAction is not None, "parseNonceCallback: lastAction is None"
#     assert dataset is not None, "addNonceCallback: dataset is None"
#     assert queues is not None, "parseNonceCallback: queues is None"
#     assert archivePath is not None, "parseNonceCallback: archivePath is None"
#     assert archiveSystem is not None, \
#         "parseNonceCallback: archiveSystem is None"
#     assert manifestURL is not None, "parseNonceCallback: manifestURL is None"
#     assert pipeline_uuid is not None, "parseNonceCallback: pipeline_uuid is None"
#     try:
#         transcriptReference = urllib.unquote_plus(context.transcriptReference)
#     except Exception:
#         transcriptReference = None
#
#     return (lastAction, dataset, queues, archivePath, archiveSystem,
#             manifestURL, transcriptReference, pipeline_uuid)
#
# def star(r):
#     ag = r.client
#     context = r.context  # Actor context
#     (lastAction, dataset, queues, archivePath, archiveSystem,
#         manifestURL, transcriptReference, pipeline_uuid) = parseCallback(r)
#     assert transcriptReference is not None, \
#         "star: transcriptReference is None"
#
#     m = context.message_dict
def resub(r,ag):
    ag.token='94dcee9c76113147e183a2123b435e0'
    job_def = copy.copy(r.settings.echo)
    try:
        job_id = ag.jobs.submit(body=job_def)['id']
        print(json.dumps(job_def, indent=4))
    except Exception as e:
        print(json.dumps(job_def, indent=4))
        print("Error submitting job: {}".format(e))
        print(e.response.content)

    return

def main():
    """Main function"""
    r = Reactor()
    r.logger.info("Hello this is actor {}".format(r.uid))


    r = Reactor()
    #xnonce = r.add_nonce(permission='EXECUTE', maxuses=-1)
    #print("NONCE:")
    #print(xnonce)

    ag = r.client  # Agave client

    context = r.context  # Actor context
    pprint.pprint(context)


    m = context.message_dict
    status = None
    try:
        status = context.status
        #or m['status']
    except Exception as e:
        try:
            status = m.get('status')
        except Exception as e:
            status = None

    r.logger.info("Triggered action for last action of {}".format(status))
    if status == "FINISHED":
        resub(r,ag)


    r.on_success("successfully ran")

    # m = context.message_dict
    # lastAction = None
    # try:
    #     lastAction = context.lastAction
    # except Exception as e:
    #     try:
    #         lastAction = m.get('lastAction')
    #     except Exception as e:
    #         lastAction = None
    #
    # r.logger.info("Triggered action for last action of {}".format(lastAction))
    # for action in defaultTaskPath[lastAction]:
    #     if action is not None:
    #         action(r)

    r.on_success("successfully ran")


if __name__ == '__main__':
    main()
