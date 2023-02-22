# Key
# c0zzzsd9sww_cGRqeMBRhmoqkDnsJrEBbnD1pqpEdusD

from deta import Deta  # Import Deta

DETA_PROJECT_KEY = "c0zzzsd9sww_cGRqeMBRhmoqkDnsJrEBbnD1pqpEdusD"

# Initialize with a Project Key
deta = Deta(DETA_PROJECT_KEY)

# Bases 
ClassesCollection = deta.Base("Classes")
BooksCollection = deta.Base("Books")
SubjectsCollection = deta.Base("Subjects")
