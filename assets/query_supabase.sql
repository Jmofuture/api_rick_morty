
CREATE TABLE youtube_channels (
  channel_id VARCHAR(50) NOT NULL PRIMARY KEY,
  creation_date timestamp WITH TIME ZONE,
  channel_name VARCHAR(100) NOT NULL,
  country VARCHAR(5),
  subscribers INT,
  videos INT,
  views INT
);

CREATE INDEX idx_channel_name ON youtube_channels (channel_name);