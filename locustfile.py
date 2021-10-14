import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get('/')

    @task(3)
    def multiply(self):
        for i in range(10):
            for j in range(10):
                self.client.get(f'/calc/mul?m={i}&n={j}', name='/calc/mul')

    @task(3)
    def sum(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.client.get(f'/calc/sum?m={i}&n={j}', name='/calc/sum')

    @task(3)
    def sum(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.client.get(f'/calc/sub?m={i}&n={j}', name='/calc/sub')

    @task(3)
    def divide(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.client.get(f'/calc/div?m={i}&n={j}', name='/calc/div')

    def on_start(self):  # init for each virtual user
        pass

    
