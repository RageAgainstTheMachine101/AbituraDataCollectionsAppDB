from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from graphviz import Digraph
from apps.base_entities.models import BaseEntity

# Create the SQLAlchemy engine
DATABASE_URL = "sqlite:///mydatabase.db"
engine = create_engine(DATABASE_URL)

# Function to generate ER diagram
def generate_er_diagram(base):
    dot = Digraph(comment='ER Diagram')

    inspector = inspect(engine)

    # Add nodes for each table
    for table_name in inspector.get_table_names():
        dot.node(table_name, table_name)
        print(f"Added node for table: {table_name}")

    # Add edges for each relationship
    for table_name in inspector.get_table_names():
        foreign_keys = inspector.get_foreign_keys(table_name)
        for foreign_key in foreign_keys:
            referenced_table = foreign_key['referred_table']
            dot.edge(table_name, referenced_table)
            print(f"Added edge from {table_name} to {referenced_table}")

    dot.render('consolidated_erd', format='pdf')

# Generate the ER diagram
generate_er_diagram(BaseEntity)
