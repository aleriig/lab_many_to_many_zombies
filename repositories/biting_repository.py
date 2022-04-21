from db.run_sql import run_sql
from models.biting import Biting
from models.human import Human
from models.zombie import Zombie
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository

def save(biting):
    sql = "INSERT INTO bitings (zombie_id, human_id) VALUES (%s, %s) RETURNING id"
    values = [biting.zombie.id, biting.human.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id

def select_all():
    bitings = []

    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for result in results:
        human = human_repository.select(result['human_id'])
        zombie = zombie_repository.select(result['zombie_id'])
        biting = Biting(human, zombie)
        bitings.append(biting)
    return bitings

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    human = human_repository.select(result["human_id"])
    zombie = zombie_repository.select(result["zombie_id"])
    biting = Biting(human, zombie, result["id"])
    return biting

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def update(biting):
    sql = "UPDATE biting SET (human_id, zombie_id) = (%s, %s) WHERE id = %s"
    values = [biting.human.id, biting.zombie.id, biting.id]
    run_sql(sql, values)



