from sqlalchemy import create_engine, inspect
from apps.base_entities.models import BaseEntity
import eralchemy

# Create the SQLAlchemy engine
DATABASE_URL = "sqlite:///mydatabase.db"
engine = create_engine(DATABASE_URL)

# Function to generate ER diagram
def generate_er_diagram(base):
    # Generate the ER diagram using ERAlchemy
    eralchemy.render_er(DATABASE_URL, 'consolidated_erd.png')

# Generate the ER diagram
generate_er_diagram(BaseEntity)
