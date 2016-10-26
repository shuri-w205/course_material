(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn wordcount [options]
   [
    ;; spout configuration
    {"word-spout" (python-spout-spec
          options
          "spouts.words.WordSpout"
          ["time" "word"] 
          )
     "data-spout" (python-spout-spec
          options
          "spouts.words.DataSpout"
          ["time" "data"] 
          )
    }
    ;; bolt configuration
    {"count-bolt" (python-bolt-spec
          options
          {
             ;; TODO Read both sources into DataCruncher.
          }
          "bolts.wordcount.DataCruncher"
          ["time" "score"]
          :p 2
          )
    }
  ]
)
