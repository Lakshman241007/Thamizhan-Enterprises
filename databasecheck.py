from supabase import create_client, Client

import os


SUPABASE_URL = os.getenv("SUPA_URL")
SUPABASE_KEY = os.getenv("SUPA_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

data={
    "Full Name":"Sid",
    "Password":"weis82339",
    "Email":"kk12331@gmail.com"}

response=supabase.table("Employee_details").insert(data).execute()
