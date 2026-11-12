import { supabase } from './supabase.js'

export async function signUpStudent(data) {
  const { data: authData, error: authError } = await supabase.auth.signUp({
    email: data.email,
    password: data.password,
  })
  if (authError) throw authError

  const userId = authData.user?.id
  if (!userId) throw new Error("User create nahi ho saka")

  const { error: profileError } = await supabase.from('profiles').insert({
    id: userId,
    display_name: data.display_name,
    email: data.email,
    school_name: data.school_name,
    grade_level: data.grade_level,
    is_under_18: data.age < 18,
    guardian_email: data.age < 18 ? data.guardian_email : null,
    guardian_verified: data.age >= 18,
    seller_level: 1,
    esg_xp: 0,
    strikes: 0,
  })
  if (profileError) throw profileError

  return { success: true, needsGuardian: data.age < 18 }
}

export async function loginStudent(email, password) {
  const { data, error } = await supabase.auth.signInWithPassword({ email, password })
  if (error) throw error
  return data
}