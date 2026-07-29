def summary(subjects, tasks):

    completed = sum(
        1
        for task in tasks
        if task.get("completed")
    )

    return {
        "subjects": len(subjects),
        "tasks": len(tasks),
        "completed": completed
    }
