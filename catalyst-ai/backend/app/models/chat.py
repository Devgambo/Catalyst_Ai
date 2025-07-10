from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON, Float, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from . import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Chat settings
    is_active = Column(Boolean, default=True, nullable=False)
    is_archived = Column(Boolean, default=False, nullable=False)
    
    # Metadata
    metadata = Column(JSON, nullable=True)  # Store additional chat settings
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="chats")
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="chat", cascade="all, delete-orphan")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"), nullable=False)
    
    # Message content
    content = Column(Text, nullable=False)
    role = Column(String(20), nullable=False)  # 'user' or 'assistant'
    
    # Message metadata
    token_count = Column(Integer, nullable=True)
    processing_time = Column(Float, nullable=True)  # in seconds
    
    # Context and sources
    context_documents = Column(JSON, nullable=True)  # Referenced document IDs
    source_chunks = Column(JSON, nullable=True)  # Referenced chunk IDs
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    chat = relationship("Chat", back_populates="messages")

# Composite indexes for common queries
Index("idx_messages_chat_created", Message.chat_id, Message.created_at)