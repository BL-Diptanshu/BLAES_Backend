# from sqlalchemy import (
#     Column, String, Enum, Text, DECIMAL, Integer, JSON,
#     Boolean, ForeignKey
# )
# from sqlalchemy.dialects.mysql import TIMESTAMP
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from app.config.database import Base
# import enum

# class QuestionType(str, enum.Enum):
#     ASSIGNMENT = "ASSIGNMENT"
#     LAB        = "LAB"
#     SELF       = "SELF"
#     TEST       = "TEST"

# class AnswerType(str, enum.Enum):
#     MCQ          = "MCQ"
#     MULTI_SELECT = "MULTI_SELECT"
#     NUMERIC      = "NUMERIC"
#     TEXT         = "TEXT"
#     CODE         = "CODE"
#     MATCHING     = "MATCHING"

# class Difficulty(str, enum.Enum):
#     EASY   = "EASY"
#     MEDIUM = "MEDIUM"
#     HARD   = "HARD"


# class Programme(Base):
#     __tablename__ = "programme"

#     id = Column(String(36), primary_key=True)
#     name = Column(String(255), nullable=False)
#     created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())

#     modules = relationship("Module", back_populates="programme")


# class Module(Base):
#     __tablename__ = "module"

#     id = Column(String(36), primary_key=True)
#     programme_id = Column(
#         String(36), ForeignKey("programme.id", ondelete="RESTRICT"), nullable=False
#     )
#     name = Column(String(255), nullable=False)
#     created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())

#     programme   = relationship("Programme", back_populates="modules")
#     sub_modules = relationship("SubModule", back_populates="module")


# class SubModule(Base):
#     __tablename__ = "sub_module"

#     id = Column(String(36), primary_key=True)
#     module_id = Column(
#         String(36), ForeignKey("module.id", ondelete="RESTRICT"), nullable=False
#     )
#     name = Column(String(255), nullable=False)
#     created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())

#     module      = relationship("Module", back_populates="topics")
#     sub_modules = relationship("SubModule", back_populates="topic")


# class Question(Base):
#     __tablename__ = "questions"

#     id = Column(String(36), primary_key=True)
#     programme_id = Column(
#         String(36), ForeignKey("programme.id", ondelete="RESTRICT"), nullable=False
#     )
#     module_id = Column(
#         String(36), ForeignKey("module.id", ondelete="RESTRICT"), nullable=False
#     )
#     submodule_id = Column(
#         String(36), ForeignKey("sub_module.id", ondelete="RESTRICT"), nullable=False
#     )
    
#     question_type = Column(Enum(QuestionType), nullable=False)
#     answer_type   = Column(Enum(AnswerType), nullable=False)
#     difficulty    = Column(Enum(Difficulty), nullable=False, default=Difficulty.MEDIUM)

#     stem_md      = Column(Text, nullable=False)
#     solution_md  = Column(Text)
#     score_weight = Column(DECIMAL(6, 2), nullable=False, default=1.00)
#     metadata_json = Column(JSON)
#     version      = Column(Integer, nullable=False, default=1)
#     is_current   = Column(Boolean, nullable=False, default=True)

#     created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())
#     updated_at = Column(
#         TIMESTAMP(fsp=3),
#         server_default=func.now(),
#         onupdate=func.now()
#     )

#     programme  = relationship("Programme")
#     module     = relationship("Module")
#     sub_modules = relationship("SubModule")


from sqlalchemy import (
    Column, String, Enum, Text, DECIMAL, Integer, JSON,
    Boolean, ForeignKey
)
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base
import enum

# -----------------------------------------
# ENUM DEFINITIONS
# -----------------------------------------
class QuestionType(str, enum.Enum):
    ASSIGNMENT = "ASSIGNMENT"
    LAB        = "LAB"
    SELF       = "SELF"
    TEST       = "TEST"

class AnswerType(str, enum.Enum):
    MCQ          = "MCQ"
    MULTI_SELECT = "MULTI_SELECT"
    NUMERIC      = "NUMERIC"
    TEXT         = "TEXT"
    CODE         = "CODE"
    MATCHING     = "MATCHING"

class Difficulty(str, enum.Enum):
    EASY   = "EASY"
    MEDIUM = "MEDIUM"
    HARD   = "HARD"


# -----------------------------------------
# PROGRAMME
# -----------------------------------------
class Programme(Base):
    __tablename__ = "programme"

    id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())

    # 1 Programme → Many Modules
    modules = relationship("Module", back_populates="programme")


# -----------------------------------------
# MODULE
# -----------------------------------------
class Module(Base):
    __tablename__ = "module"

    id = Column(String(36), primary_key=True)
    programme_id = Column(
        String(36),
        ForeignKey("programme.id", ondelete="RESTRICT"),
        nullable=False
    )
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())

    # Relation to Programme
    programme = relationship("Programme", back_populates="modules")

    # 1 Module → Many SubModules
    submodules = relationship("SubModule", back_populates="module")


# -----------------------------------------
# SUBMODULE
# -----------------------------------------
class SubModule(Base):
    __tablename__ = "sub_module"

    id = Column(String(36), primary_key=True)
    module_id = Column(
        String(36),
        ForeignKey("module.id", ondelete="RESTRICT"),
        nullable=False
    )
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())

    # Relation to parent module
    module = relationship("Module", back_populates="submodules")

    # 1 SubModule → Many Questions
    questions = relationship("Question", back_populates="submodule")


# -----------------------------------------
# QUESTION
# -----------------------------------------
class Question(Base):
    __tablename__ = "questions"

    id = Column(String(36), primary_key=True)

    programme_id = Column(
        String(36),
        ForeignKey("programme.id", ondelete="RESTRICT"),
        nullable=False
    )
    module_id = Column(
        String(36),
        ForeignKey("module.id", ondelete="RESTRICT"),
        nullable=False
    )
    submodule_id = Column(
        String(36),
        ForeignKey("sub_module.id", ondelete="RESTRICT"),
        nullable=False
    )

    # Enum columns
    question_type = Column(Enum(QuestionType), nullable=False)
    answer_type   = Column(Enum(AnswerType), nullable=False)
    difficulty    = Column(Enum(Difficulty), nullable=False, default=Difficulty.MEDIUM)

    stem_md      = Column(Text, nullable=False)
    solution_md  = Column(Text)
    score_weight = Column(DECIMAL(6, 2), nullable=False, default=1.00)
    metadata_json = Column(JSON)

    version      = Column(Integer, nullable=False, default=1)
    is_current   = Column(Boolean, nullable=False, default=True)

    created_at = Column(TIMESTAMP(fsp=3), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(fsp=3),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    programme = relationship("Programme")
    module    = relationship("Module")
    submodule = relationship("SubModule", back_populates="questions")
