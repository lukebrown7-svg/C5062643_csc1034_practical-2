from job import Job
from job_manager import JobManager

print("Normal Case Test")
jm = JobManager()
job1 = Job("Luke","Student",10.0,"12/12/12",2)
print(jm.add_job(job1))

print("Erroneous Case Test 1")
job2 = Job("Luke","Student",10.0,"12/12/12",7)
print(jm.add_job(job2))

print("Boundary Case Test 1")
job3 = Job("James","Student",10.0,"12/12/12",6)
print(jm.add_job(job3))
print(jm.get_jobs())

print("Exceptional Case Test")
job4 = Job("Joe","Teacher","notanumber","12/12/12","notanumber")
print(jm.add_job(job4))






