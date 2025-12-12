from job import Job
from job_manager import JobManager

print("Normal Case Test")
jm = JobManager()
job1 = Job("Luke","Student",10.0,"12/12/12",2)
print(jm.add_job(job1))
print(jm.get_jobs())



