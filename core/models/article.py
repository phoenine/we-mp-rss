from  .base import Base,Column,String,Integer,DateTime,Text,DATA_STATUS
class ArticleBase(Base):
    from_attributes = True
    __tablename__ = 'articles'
    id = Column(String(255), primary_key=True)
    mp_id = Column(String(255))
    title = Column(String(1000))
    pic_url = Column(String(500))
    url=Column(String(500))
    description=Column(Text)
    status = Column(Integer,default=1)
    publish_time = Column(Integer,index=True)
    publish_at = Column(DateTime, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_export = Column(Integer)
class Article(ArticleBase):
    content = Column(Text)
