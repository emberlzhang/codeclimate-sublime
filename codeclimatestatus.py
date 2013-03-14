import sublime, sublime_plugin, threading, json, os

class CodeClimateStatusListener(sublime_plugin.EventListener):
  #start getting CodeClimate ratings when file loads
  def on_load(self, view):
    #TODO: change to 'source.ruby' when everything else works
    if 'source.ruby' not in view.scope_name(0):
      return
    view.run_command('code_climate_status')

class CodeClimateStatusCommand(sublime_plugin.TextCommand):
  def run(self, edit):
  #--------------------------------------klasses
  #find all klasses in directory
    #klasses =
  #make each klass a thread
    #threads = []
    #for klass in klasses
      #thread = CodeClimateAPICall() 
      #threads.apprend(thread)
      #threads.start()
  #clear the klasses
    #self.view.klass().clear() #klass or klasses?
  #make codeclimate key object
  #--------------------------------------threads
  #handle all threads
  #next_threads
  #for thread in threads:
    #if thread.is_alive():
      #next_threads.append(thread)
      #continue
    #if thread.result == False:
      #continue
  #threads = next_threads
  #--------------------------------------
    #plugin_settings = sublime.load_settings('CodeClimateStatus.sublime-theme')

    grade = "D"
    old_gutter_grade = self.view.get_regions('gutter-grade')

    self.view.sel().clear()

    self.view.erase_regions('gutter-grade')
    self.view.add_regions('gutter-grade', [sublime.Region(self.view.text_point(0, 0))], 'constant', self.bookmark_path(grade))
    # self.view.add_regions('gutter-grade-b', [sublime.Region(self.view.text_point(1, 0))], 'constant', '../CodeClimateStatus/img/letterB')
    # self.view.add_regions('gutter-grade-c', [sublime.Region(self.view.text_point(2, 0))], 'constant', '../CodeClimateStatus/img/letterC')
    # self.view.add_regions('gutter-grade-d', [sublime.Region(self.view.text_point(3, 0))], 'constant', '../CodeClimateStatus/img/letterD')

    klass = "ExampleClass"
    complexity = "LOW"
    complexity_per_method = "LOW"
    duplication = "LOW"
    churn = "MED"
    status = "<<< CodeClimate Ratings for Class \"%s\" || Complexity: %s | Complexity/Method: %s | Duplication: %s | Churn: %s || >>>" %(klass, complexity, complexity_per_method, duplication, churn)
    self.view.set_status('code-climate', status)

    print old_gutter_grade
    print find_repo_path()

  def bookmark_path(self, grade):
    return '../CodeClimateStatus/img/letter' + grade

def find_repo_path(full_name):
  print os.path.split(full_name)

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