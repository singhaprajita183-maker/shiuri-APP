import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const supabaseUrl = 'https://cltgmbptrayrrenflktz.supabase.co'
const supabaseAnonKey = sb_publishable_AqV3ngsG79JifY16ZhBkzA_cC8RE88s
export const supabase = createClient(supabaseUrl, supabaseAnonKey)