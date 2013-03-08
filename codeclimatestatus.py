import sublime, sublime_plugin, threading, json

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

    grade = "A"
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

  def bookmark_path(self, grade):
    return '../CodeClimateStatus/img/letter' + grade


#on_load
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