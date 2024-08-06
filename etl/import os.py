import os
import pandas as pd
import numpy as np
from faker import Faker
# Ensure custom_providers module is in the project directory
# from custom_providers import NYCAddressProvider, NYCPersonProvider, RentalDescriptionProvider, PropertyAmenitiesProvider, ExtendedZipcodeProvider
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random

# Initialize Faker
fake = Faker()

# Example usage of Faker to generate random names
for _ in range(5):
    print(fake.name())
