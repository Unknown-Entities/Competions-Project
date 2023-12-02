from App.models import User, Ranking, User_Competition
from App.database import db
from .profile import get_profile


def get_rank(id):
    return Ranking.query.get(id)

def create_ranking(profile_id, name, rank, points):
    ranking = Ranking(profile_id=profile_id, name=name, rank=rank, points=points)
    try:
        db.session.add(ranking)
        db.session.commit()
        return ranking
    except:
        return None

def calculate_ranking():
    ranks = get_rankings()
    all_ranks = sorted(ranks, key=lambda x: x.points, reverse=True)
    for ranks in all_ranks:
        findrank = Ranking.query.filter_by(points=ranks.points).first()
        profile = get_profile(findrank.id)
        findrank.rank = all_ranks.index(ranks) + 1
        profile.Ranking = findrank.rank
        db.session.add(findrank)
        db.session.add(profile)
        db.session.commit()


def add_ranking(profile_id, name):  # ranking):
    newrank = Ranking(profile_id=profile_id, name=name,
                      points=0, rank=0)
    db.session.add(newrank)
    db.session.commit()
    return newrank


def get_rankings():
    return Ranking.query.all()


def get_rankings_json():
    ranks = get_rankings()
    if not ranks:
        return []
    ranks = sorted(ranks, key=lambda rank: rank.points, reverse=True)

    send = []
    for rank in ranks:
        add = rank.get_json()
        index = ranks.index(rank) + 1
        if add["Points"] == 0:
            continue

        ranking = get_rank(add["ID"])
        user = User.query.get(add["ID"])
        ranking.rank = index
        user.rank = index

        db.session.add(user)
        db.session.add(ranking)
        db.session.commit()

        send.append(add)

    return send


def get_top_20_users_rank():
    top = []
    for num in range(1, 20):
        findrank = Ranking.query.filter_by(rank=num).first()
        if findrank:
            rank = findrank.get_json()
            top.append(rank)

    return top

def get_user_rankings(user_id):
    users = User.query.get(user_id)
    userComps = users.competitions
    ranks = [User_Competition.query.get(a.id).toJSON() for a in userComps]
    return ranks

def get_profile_ranking(id):
    rank = Ranking.query.filter_by(profile_id=id).first()
    return rank

def calculate_ranking_points(rank):
    if rank == 1:
        return "100"
    elif rank == 2:
        return "80"
    elif rank == 3:
        return "60"
    elif rank == 4:
        return "50"
    elif rank == 5:
        return "40"
    elif rank == 6:
        return "30"
    elif rank == 7:
        return "20"
    elif rank == 8:
        return "25"
    elif rank == 9:
        return "20"
    elif rank >= 10:
        return "15"