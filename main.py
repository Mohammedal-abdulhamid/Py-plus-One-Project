from fastapi import FastAPI, HTTPException
import json
import psycopg2

app = FastAPI()


@app.get("/api/events")
def det_events():
    conn = psycopg2.connect(dbname="nc_plus_one_project", host="localhost")
    cursor = conn.cursor()
    sql_select_tables = "SELECT * FROM events ORDER BY starts_at;"
    cursor.execute(sql_select_tables)
    events = cursor.fetchall()
    if  events is None:
        raise HTTPException(detail="No events found")

    cursor.close()
    conn.close()
    return {"events" : events}


@app.get("/api/events/{event_id}")
def get_event(event_id: int):
    conn = psycopg2.connect(dbname="nc_plus_one_project", host="localhost")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events WHERE id = %s;",
        (event_id,))
    event = cursor.fetchone()
    cursor.close()
    conn.close()
    if event is None:
        raise HTTPException(
            status_code=404,
            detail=f"Event with id {event_id} not found."
        )
    
    event = {
        "id": event[0],
        "title": event[1],
        "description": event[2],
    }
    return event