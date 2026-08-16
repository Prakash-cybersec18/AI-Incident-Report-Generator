def show_progress(stage, progress):
    total = 20
    filled = int(total * progress / 100)
    bar = "█" * filled + "░" * (total - filled)

    print(f"{stage:<25} [{bar}] {progress:>3}%")


def show_overall_progress(completed, total, incident_id):
    if total == 0:
        progress = 0
    else:
        progress = int((completed / total) * 100)

    bar_length = 30
    filled = int(bar_length * progress / 100)

    bar = "█" * filled + "░" * (bar_length - filled)

    print(
        f"Overall {incident_id}: "
        f"[{bar}] {progress:>3}%"
    )