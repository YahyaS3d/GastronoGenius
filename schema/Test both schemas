-- Supabase AI is experimental and may produce incorrect answers
-- Always verify the output before executing

create extension if not exists "uuid-ossp";

insert into
  recipes (
    user_id,
    title,
    description,
    content_json,
    ingredients,
    difficulty,
    cooking_time,
    people,
    low_calories,
    vegan,
    paleo,
    calories,
    proteins,
    fats,
    carbs
  )
values
  (
    uuid_generate_v4 (),
    'Sample Recipe',
    'This is a sample recipe description.',
    '{"steps": ["Step 1", "Step 2", "Step 3"]}',
    '[{"ingredient": "Sample Ingredient 1", "quantity": "100g"}, {"ingredient": "Sample Ingredient 2", "quantity": "200g"}]',
    'Easy',
    30,
    4,
    true,
    false,
    false,
    500,
    20,
    10,
    60
  );
