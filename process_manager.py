
from file_downloader import FileDownloader
from bot_reply_manager import BotReplyManager

# Maximum number of image processes running async
maxActiveJobs = 3

class ProcessManager:

  def __init__(self):

    # All of the jobs which will be attached
    self.job_list = []

    # Used for controlling the queue
    self.current_active_jobz = 0

  """ Job is {message_id, isQueued, message} """
  def add_job(self, job):

    # Check if the message_id already exists
    is_found = False

    for job_search in self.job_list:

      print(f" Requested Job MessageId: {job['messageId']} and searchId is {job_search['messageId']}")

      if job["messageId"] == job_search["messageId"]:
        is_found = True
        
    if not is_found:
      self.job_list.append(job)
      
    self.next_job()

  """ When a job is finished this guy get's called """
  def next_job(self):

    if self.current_active_jobz < maxActiveJobs:
      self.start_a_job()

  def start_a_job(self):

    current_job = None

    for job in self.job_list:
      if current_job == None and not job["isQueued"] and not job["isFinished"]:

        self.current_active_jobz += 1

        job["isQueued"] = True

        current_job = job

    print(f"Current Job is:{current_job}")

    if current_job != None:

      message = current_job["message"]

      downloader = FileDownloader(message, self) 

      # Start the image process by downloading the image
      downloader.get_file_path()   
    