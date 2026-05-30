CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Seed data so the directory isn't empty on first load
INSERT INTO employees (name, department, role, email) VALUES
    ('Amara Nwosu', 'Engineering', 'Cloud Security Engineer', 'amara.nwosu@company.com'),
    ('Chidi Okafor', 'DevOps', 'Infrastructure Engineer', 'chidi.okafor@company.com'),
    ('Fatima Al-Hassan', 'Product', 'Product Manager', 'fatima.alhassan@company.com'),
    ('Emeka Eze', 'Security', 'SOC Analyst', 'emeka.eze@company.com'),
    ('Ngozi Adeyemi', 'Engineering', 'Backend Engineer', 'ngozi.adeyemi@company.com');
