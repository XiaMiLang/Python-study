# Write your code here
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Task(Base):
    __tablename__ = "task"
    id = Column("id", Integer, primary_key=True)
    task = Column("task", String)
    deadline = Column("deadline", Date, default=datetime.today())

    def __repr__(self):
        return "{}. {}".format(self.id, self.task)


engine = create_engine('sqlite:///todo.db?check_same_thread=False', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


flag = True


def to_print():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")


while flag:
    to_print()
    selection = input()
    if selection == "0":
        print("Bye!")
        exit()
    if selection == "1":
        rows = session.query(Task).all()
        count = 0
        for r in rows:
            if r.deadline == datetime.today().date():
                count += 1
        # if new_row.task is None:
        if count == 0:
            print("Today {} {}:".format(datetime.today().day, datetime.today().strftime('%b')))
            print("Nothing to do!")
            print()
        else:
            print("Today {} {}:".format(datetime.today().day, datetime.today().strftime('%b')))
            index = 1
            for r in rows:
                if datetime.today().date() == r.deadline:
                    print("{}. {}".format(index, r.task))
                    index += 1
            print()

    if selection == "2":
        rows = session.query(Task).all()

        weekday = datetime.today().weekday()
        wkday = datetime.today().weekday()
        # Monday = datetime.today() - timedelta(days=wkday)
        today = datetime.today()

        for i in range(0, 7):
            task_printed = False
            print("{} {} {}:".format((today + timedelta(days=i)).strftime('%A'), (today + timedelta(days=i)).day,
                                     (today + timedelta(days=i)).strftime('%b')))
            index = 1
            for r in rows:
                if (today + timedelta(days=i)).date() == r.deadline:
                    print("{}. {}".format(index, r.task))
                    index += 1
                    task_printed = True
            if task_printed is not True:
                print("Nothing to do!")

            print()

    if selection == "3":
        rows = session.query(Task).order_by(Task.deadline).all()
        for r in rows:
            print("{}. {}".format(r, r.deadline.strftime("%#d %b")))
        print()

    if selection == "4":
        rows = session.query(Task).filter(Task.deadline < datetime.today().date()).order_by(Task.deadline)
        # rows = session.query(Task).order_by(Task.deadline)all()
        if rows == "":
            print("Nothing is missed!")
        else:
            print("Missed tasks:")
            index = 1
            for r in rows:
                print("{}. {}. {}".format(index, r.task, r.deadline.strftime("%#d %b")))
                index += 1
        print()

    if selection == "5":
        print("Enter task")
        new_row = Task()
        new_row.task = input()
        print("Enter deadline")
        new_row.deadline = datetime.strptime(input(), '%Y-%m-%d')
        print("The task has been added!")
        session.add(new_row)
        session.commit()
        print()

    if selection == "6":
        rows = session.query(Task).order_by(Task.deadline).all()
        if rows != "":
            index = 1
            print("Choose the number of the task you want to delete:")
            for r in rows:
                print("{}. {}. {}".format(index, r.task, r.deadline.strftime("%#d %b")))
                index += 1
            to_delete = int(input())
            specific_row = rows[to_delete - 1]
            session.delete(specific_row)
            session.commit()
            print("The task has been deleted!")

            print()

        else:
            print("Nothing to delete")
            print()

