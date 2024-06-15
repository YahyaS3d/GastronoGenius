CREATE TABLE IF NOT EXISTS recipes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID,
  title TEXT NOT NULL,
  description TEXT,
  content_json JSONB,
  ingredients JSONB,
  difficulty TEXT,
  cooking_time INTEGER,
  people INTEGER,
  low_calories BOOLEAN,
  vegan BOOLEAN,
  paleo BOOLEAN,
  calories INTEGER,
  proteins INTEGER,
  fats INTEGER,
  carbs INTEGER,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
