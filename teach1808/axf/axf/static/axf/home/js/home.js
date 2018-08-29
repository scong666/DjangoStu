$(function () {
    // 初始化
    init_top_swiper(),
    init_must_swiper()
})

function init_top_swiper() {
    var mySwiper = new Swiper('#topSwiper', {
        // direction: 'vertical', #竖排
        // 循环
        loop: true,
        //1.5秒播放
        autoplay:1500,
        // 如果需要分页器
        pagination: '.swiper-pagination',
        // 如果需要前进后退按钮
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
    })
}

function init_must_swiper() {
    var mySwiper = new Swiper('#swiperMenu', {
         slidesPerView:3,
    })
}l