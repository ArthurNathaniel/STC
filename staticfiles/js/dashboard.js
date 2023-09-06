        const total = document.getElementById('tm');
        new Chart(total, {
            type: 'bar',
            data: {
                labels: ['Total Population'],
                datasets: [{
                    label: 'Total Members',
                    data: [{{ total_members }}],
                borderWidth: 1
            }]
        },
            });
  
        const ctx = document.getElementById('myChart');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Male', 'Female'],
                datasets: [{
                    label: 'Member(s)',
                    data: [{{ male_count }}, {{ female_count }}],
            borderWidth: 1
        }]
             },
        });
    
        const mrd = document.getElementById('myChartt');
        new Chart(mrd, {
            type: 'doughnut',
            data: {
                labels: ['Catholics', 'Other'],
                datasets: [{
                    label: "Mother's Denomination",
                    data: [{{ mother_catholic }}, {{ mother_other }}],
            borderWidth: 1
        }]
             },
        });
   
        const frd = document.getElementById('father');
        new Chart(frd, {
            type: 'doughnut',
            data: {
                labels: ['Catholics', 'Other'],
                datasets: [{
                    label: "Father's Denomination",
                    data: [{{ father_catholic }}, {{ father_other }}],
            borderWidth: 1
        }]
             },
        });
   
        const ms = document.getElementById('ms');
        new Chart(ms, {
            type: 'doughnut',
            data: {
                labels: ['Single', 'Married', 'Divorced', 'Annualled', 'Widowed'],
                datasets: [{
                    label: "Martial Status",
                    data: [{{ single }}, {{ married }}, {{ divorced }}, {{ annualled }}, {{ widowed }}],
            borderWidth: 1
    }]
             },
        });
  
        const im = document.getElementById('im');
        new Chart(im, {
            type: 'pie',
            data: {
                labels: ['Holy Matrimony', 'Traditional Marriage', 'None'],
                datasets: [{
                    label: "If Married",
                    data: [{{ holy }}, {{ traditional }}],
            borderWidth: 1
    }]
             },
        });