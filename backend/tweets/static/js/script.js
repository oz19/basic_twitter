        var ENDPOINT = 'http://localhost:8000/api/v1/tweets/';

        function getCookie(name) {
            if (!document.cookie) {
                return null;
            }

            const xsrfCookies = document.cookie.split(';')
                .map(c => c.trim())
                .filter(c => c.startsWith(name + '='));

            if (xsrfCookies.length === 0) {
                return null;
            }
            return decodeURIComponent(xsrfCookies[0].split('=')[1]);
        }

        // Get all tweets
        const tweetList = new Vue({
            el      : '#tweetList',
            data    : {
                tweets: [],
            },

            created () {
                fetch(ENDPOINT)
                    .then(response => response.json())
                    .then(data => {
                        this.tweets = data;
                    })
            }

        });

        // Post a tweet
        const postTweet = new Vue({
            el      : '#postTweet',
            data    : {
                name    : '',
                text    : '',
            },

            methods : {
                send: function(event){
                    event.preventDefault();
                    var payload = {
                        name: this.name,
                        text: this.text
                    }
                    let headers = {
                        'X-CSRFToken': getCookie('csrftoken')
                    };

                    // send post request
                    this.$http.post(ENDPOINT, payload, {headers: headers})
                        .then( (data, status, request) => {
                            this.response = data;
                            location.reload();
                        })
                        .catch( (data, status, request) => {
                            console.log(data);
                        });

                }
            }
        });

