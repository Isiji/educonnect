#!/usr/bin/python3
"""Student module for the student model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(BaseModel, Base):
    """Student model"""
    __tablename__ = 'students'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='students')
    class_id = Column(String(60), ForeignKey('classes.id'), nullable=False)
    classes = relationship('Class', back_populates='students')
    assignments = relationship('Assignment', back_populates='student')

    def __init__(self, *args, **kwargs):
        """initializes the student"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """string representation of the student"""
        return "Student: {} {}".format(self.first_name, self.last_name)