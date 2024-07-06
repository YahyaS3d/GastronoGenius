CREATE TABLE IF NOT EXISTS generations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  content_json JSONB,
  title TEXT NOT NULL,
  difficulty TEXT,
  cooking_time INTEGER,
  people INTEGER,
  low_calories BOOLEAN,
  vegan BOOLEAN,
  paleo BOOLEAN,
  description TEXT,
  calories INTEGER,
  proteins INTEGER,
  fats INTEGER,
  carbs INTEGER,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
