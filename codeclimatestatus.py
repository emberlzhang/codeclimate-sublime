import sublime, sublime_plugin, subprocess, json, os

class CodeClimateStatusListener(sublime_plugin.EventListener):
  def on_load(self, view):
    if 'source.ruby' not in view.scope_name(0):
      return
    view.run_command('code_climate_status')

class CodeClimateStatusCommand(sublime_plugin.TextCommand):
  def run(self, edit):
  #--------------------------------------make threads for a class
    #thread = CodeClimateAPICall() 
    #threads.apprend(thread)
    #threads.start()
  #clear the klasses
    #self.view.klass().clear() #klass or klasses?
  #make codeclimate key object
  #--------------------------------------threads
  #if thread.is_alive():
    #continue
  #if thread.result == False:
    #thread = nil
  #--------------------------------------
    #plugin_settings = sublime.load_settings('CodeClimateStatus.sublime-theme')

    grade = "D"
    old_gutter_grade = self.view.get_regions('gutter-grade')

    self.view.sel().clear()
    self.view.erase_regions('old_gutter-grade')
    self.view.add_regions('gutter-grade', [sublime.Region(self.view.text_point(0, 0))], 'constant', self.bookmark_path(grade))

    klass = "ExampleClass"
    complexity = "LOW"
    complexity_per_method = "LOW"
    duplication = "LOW"
    churn = "MED"
    status = "<<< CodeClimate Ratings for Class \"%s\" || Complexity: %s | Complexity/Method: %s | Duplication: %s | Churn: %s || >>>" %(klass, complexity, complexity_per_method, duplication, churn)
    self.view.set_status('code-climate', status)

    print old_gutter_grade
    
    #get full file path
    full_path = self.view.file_name()
    local_dir = local_repo_path(full_path)
    print remote_repo_path(local_dir)

  def bookmark_path(self, grade):
    return '../CodeClimateStatus/img/letter' + grade

def local_repo_path(original_path):
  return "bookshelf"
  #original_path eg. "/Users/janet/bookshelf/app/models/book.rb"
  #print os.path.split(full_name)
  #result eg. "bookshelf"

def remote_repo_path(local_repo):
  os.chdir('../bookshelf/')
  git_command = ["git", "config", "--get", "remote.origin.url"]
  popen = subprocess.Popen(git_command, stdout = subprocess.PIPE)
  return popen.communicate()[0].strip()

# class CodeClimateAPICall(threading.Thread):
#   def __init__(self, klass, timeout):
#     self.klass = klass
#     self.result = None
#     threading.Thread.__init__(self)
#   def run(self):
#     try:
#       url = "http://github.com/api/json"
#       params = dict(
#         )
#       response = requests.get(url=url, params=params)
#       data = json.load(response)
#       return