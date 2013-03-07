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
    plugin_settings = sublime.load_settings('CodeClimateStatus.sublime-theme')

    klass = "ExampleClass"
    grade = "A"
    reasons = "LOW duplication, LOW method complexity, LOW total complexity"
    status = "<<< CodeClimate Grade for Class, %s: %s ||| Reasons: %s >>>" %(klass, grade, reasons)
    self.view.set_status('code-climate', status)


  #--------------------------------------

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