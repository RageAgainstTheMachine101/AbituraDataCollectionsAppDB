![consolidated_erd](https://github.com/user-attachments/assets/69ac4cd6-7865-4257-9de9-70c3e83050f8)

# Review

The database schema is in 3.5NF because:
- ✅ All tables satisfy 1NF (atomic values, no repeating groups)
- ✅ All tables satisfy 2NF (no partial dependencies)
- ✅ All tables satisfy 3NF (no transitive dependencies)
- ✅ All tables satisfy BCNF (every determinant is a candidate key)

## 1. [`Base Structure`](https://github.com/RageAgainstTheMachine101/AbituraDataCollectionsAppDB/blob/main/apps/base_entities/models.py) ✅
All tables inherit from `BaseEntity` with a primary key `id`.

## 2. [`Users Module`](https://github.com/RageAgainstTheMachine101/AbituraDataCollectionsAppDB/blob/main/apps/users/models.py) ✅

### 2.1. `users`: In 3.5NF
- All attributes depend on the primary key.
- No transitive dependencies.
- No partial dependencies.

### 2.2. `user_emails`: In 3.5NF
- Properly separated from `users` table.
- Each attribute depends on the primary key.
- Email uniqueness is enforced.

### 2.3. `user_courses`: In 3.5NF
- Junction table for many-to-many relationships.
- Contains only foreign keys and a primary key.
- No transitive dependencies.

## 3. [`Courses Module`](https://github.com/RageAgainstTheMachine101/AbituraDataCollectionsAppDB/blob/main/apps/courses/models.py) ✅

### 3.1. `courses`: In 3.5NF
- All attributes directly depend on the primary key.
- No transitive dependencies.

### 3.2. `course_modules`: In 3.5NF
- Proper hierarchical relationship.
- All attributes depend on the primary key.

### 3.3. `module_lessons`: In 3.5NF
- Follows the same pattern as `course_modules`.
- Clean dependencies.

### 3.4. `lesson_steps`: In 3.5NF
- All attributes depend on the primary key.
- No partial or transitive dependencies.

## 4. [`Mood Journals Module`](https://github.com/RageAgainstTheMachine101/AbituraDataCollectionsAppDB/blob/main/apps/mood_journals/models.py) ✅

### 4.1. `mood_entries`: In 3.5NF
- Clean dependencies on the primary key.
- Proper relationship with `users`.

### 4.2. `emotion_tags`: In 3.5NF
- Simple structure with no dependency issues.

### 4.3. `mood_entry_emotion_tag`: In 3.5NF
- Proper junction table.
- Contains only necessary foreign keys.

### 4.4. `text_records` and `voice_records`: In 3.5NF
- Properly separated from `mood_entries`.
- Clear dependencies.

## 5. [`Submissions Module`](https://github.com/RageAgainstTheMachine101/AbituraDataCollectionsAppDB/blob/main/apps/submissions/models.py) ✅

### 5.1. `submissions`: In 3.5NF
- All attributes depend on the primary key.
- Proper relationships with `users` and `steps`.

### 5.2. `submission_feedback`: In 3.5NF
- Properly separated from `submissions`.
- Clear dependency on `submission_id`.

# Installation

## 1. Prerequisites

Ensure that you have the following installed:

- Python 3.11^
- pip


## 2. Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/RageAgainstTheMachine101/AbituraDataCollectionsAppDB.git
```

## 3. Navigate to the Project Directory

```bash
cd AbituraDataCollectionsAppDB
```

## 4. Install Dependencies

Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

## 5. Insert Mock Data

```bash
python [generate_mock_data.py](scripts/generate_mock_data.py)
```

## 6. Generate Tables Relations' Visualization

```bash
python [generate_erd.py](scripts/generate_erd.py)
```
