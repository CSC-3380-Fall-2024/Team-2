// HabitTypes.ts
export interface Habit {
  id: number;
  user: number;
  name: string;
  target: number;
  frequency: 'daily' | 'weekly' | 'monthly';
  created_at: string;
  updated_at: string;
  completedDays?: Set<string>; 
  streak?: number; 
}

export interface HabitLog {
  id: number;
  habit: number;
  habit_name: string;
  date: string;
  progress: number;
}